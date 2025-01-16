document.addEventListener("DOMContentLoaded", function () {
    var map = L.map('map').setView([60.1699, 24.9384], 5);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);

    // Korjaa kartan koon ongelmat
    setTimeout(function () {
        map.invalidateSize();
    }, 500);

    var markers = [];

    function fetchData(selectedYear) {
        $.getJSON('/get_data', function (data) {
            markers.forEach(marker => map.removeLayer(marker));
            markers = [];

            data.forEach(person => {
                if (person.year <= selectedYear) {
                    var popupContent = `<b>${person.name}</b><br>
                                       <a href='${person.link}' target='_blank'>Lisätietoja</a><br>
                                       <p>${person.story}</p>`;
                    var marker = L.marker([person.lat, person.lon]).addTo(map)
                        .bindPopup(popupContent);
                    markers.push(marker);
                }
            });
        });
    }

    function filterStories() {
        var input = document.getElementById('search').value.toLowerCase();
        var stories = document.getElementById('stories').getElementsByTagName('li');
    
        for (var i = 0; i < stories.length; i++) {
            var text = stories[i].textContent.toLowerCase();
            if (text.includes(input)) {
                stories[i].style.display = ''; // Show matching results
            } else {
                stories[i].style.display = 'none'; // Hide non-matching results
            }
        }
    }

    document.getElementById('year-slider').addEventListener('input', function () {
        var selectedYear = this.value;
        document.getElementById('selected-year').innerText = selectedYear;
        fetchData(selectedYear);
    });

    fetchData(1600);
});
