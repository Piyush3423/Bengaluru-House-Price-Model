async function loadLocations(){

    const response = await fetch("/locations");

    const data = await response.json();

    const select = document.getElementById("location");

    select.innerHTML = "";

    data.locations.forEach(location=>{

        let option = document.createElement("option");

        option.value = location;

        option.textContent = location;

        select.appendChild(option);

    });

}

loadLocations();

async function predictPrice(){

    const location = document.getElementById("location").value;

    const total_sqft = parseFloat(document.getElementById("sqft").value);

    const bhk = parseInt(document.getElementById("bhk").value);

    const bath = parseInt(document.getElementById("bath").value);

    const result = document.getElementById("result");

    result.innerHTML = "Predicting...";

    try{

        const response = await fetch("/predict",{

            method:"POST",

            headers:{

                "Content-Type":"application/json"

            },

            body:JSON.stringify({

                location,

                total_sqft,

                bhk,

                bath

            })

        });

        const data = await response.json();

        if(response.ok){

            result.innerHTML =
            `Estimated Price : ₹ ${data.predicted_price} Lakhs`;

        }
        else{

            result.innerHTML = data.detail;

        }

    }

    catch(error){

        result.innerHTML = "Something went wrong.";

    }

}