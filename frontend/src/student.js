import { signUpHelper } from "./student/profile.mjs";

document.addEventListener("DOMContentLoaded", function(event) {
    let qualifikationSelectors = document.querySelectorAll("div.ausbildung-checkbox input")
    qualifikationSelectors.forEach(element => {
        element.addEventListener("change", (event) => { signUpHelper.handleQualificationInput(event) })

        // To handle Mozillas brilliant idea to keep state of checkboxes on refresh, trigger dummy handler for every checkbox
        signUpHelper.handleQualificationInput({ srcElement: element });

        $("#id_availability_start").attr("type", "date");
        
    })        
});