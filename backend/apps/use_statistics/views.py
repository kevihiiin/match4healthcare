from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

import django_tables2 as tables

import os
import pandas as pd
from datetime import datetime

from django.conf import settings

logged_data_names = ["time", "status_line", "status", "request_time"]
threshold_to_filter = 50

from functools import lru_cache
import time
from apps.mapview.views import get_ttl_hash


@login_required
@staff_member_required
def use_statistics(request):
    data = process_file(ttl_hash=get_ttl_hash(60))

    table_access_count = AccessCountTable(data)
    return render(request, "view.html", {"table_access_count": table_access_count})


@lru_cache(maxsize=1)
def process_file(ttl_hash):
    requests = parse_file()
    df = pd.DataFrame(requests)
    df.columns = logged_data_names

    # TODO: Check if columns are present in dataframe
    df["status"] = df["status"].astype(float)
    df["status_line"] = df["status_line"].astype(str)
    # df['time'] = df['time'].astype(datetime)

    df_names = df
    # TODO: Can we add the index to the groupby which would make any further processing like sorting easier?
    # df['status_line'] = df.index
    groupby = df.groupby("status_line")
    groupby_keys = groupby.groups.keys()

    # Arbitrary column name of df which is not 'status_line'
    arbitrary_column_name = df_names.columns.delete(list(df_names.columns).index("status_line"))[0]
    groupby = groupby[arbitrary_column_name].count()

    # df.to_dict('index') throws TypeError "unsupported type: <class 'str'>"
    data = []
    for _, (status_line, counts) in zip(groupby_keys, groupby.items()):
        if counts > threshold_to_filter:
            data.append({"status_line": status_line, "counts": counts})

    return data


def parse_file(logfile_name="gunicorn-access.log",):
    requests = []
    with open(os.path.join(settings.RUN_DIR, logfile_name), "r") as file:
        for line in file:
            logged_data = line.split("|")
            requests.append(logged_data)
    return requests


class AccessCountTable(tables.Table):
    status_line = tables.Column()
    counts = tables.Column()

    class Meta:
        template_name = "django_tables2/bootstrap4.html"
        order_by = "-counts"
