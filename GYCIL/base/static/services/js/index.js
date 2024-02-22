jQuery(function() {
    const $modal = $("#serviceModal");

    $modal.on("show.bs.modal", function(e) {
        const $button = $(e.relatedTarget);

        const url = $button.data("url");

        fetch(url)
            .then(response => response.json())
            .then(service => {
                
                let descriptions;
                descriptions = service[0];
                
                const $modalLabel = $("#serviceModalLabel");
                const $state_city = $("#state_city");
                const $street = $("#street");
                const $cep = $("#cep");
                const $client = $("#client");
                const $description = $("#description");
                const $created_at = $("#created_at");


                $modalLabel.text(("SERVIÇO DE " + descriptions.category + ": " + descriptions.id).toUpperCase())
                $state_city.text(descriptions.state + " - " + descriptions.city);
                $street.text(descriptions.street);
                $cep.text(descriptions.cep);
                $client.text(descriptions.client.split(" ")[0] + " " + descriptions.client.split(" ")[1].slice(0,2) + "***");
                $description.text(descriptions.description);
                $created_at.text(descriptions.created_at.slice(0, 16));
       
                
            })
            .catch(console.error)
    });
    
});