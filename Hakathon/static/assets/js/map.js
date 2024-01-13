console.log("loaded");
mapboxgl.accessToken =
  "pk.eyJ1Ijoic3VzaGlsMDAxMjMiLCJhIjoiY2xyN3NlcnE1MjQ2MzJrbnY5OHB6bjE2NyJ9.GIbvDCk9iIZaCKcLV7huiw";

// Declare map globally
let map;

document.addEventListener("DOMContentLoaded", function () {
  mapboxgl.accessToken =
    "pk.eyJ1Ijoic3VzaGlsMDAxMjMiLCJhIjoiY2xyN3NlcnE1MjQ2MzJrbnY5OHB6bjE2NyJ9.GIbvDCk9iIZaCKcLV7huiw";

  map = new mapboxgl.Searc({
    container: "map", // container ID
    style: "mapbox://styles/mapbox/outdoors-v12",
    zoom: 14,
  });

  // Check browser support for geo locator
  if ("geolocation" in navigator) {
    // Get the user's current position and update the map
    navigator.geolocation.getCurrentPosition(successCallback, errorCallback, {
      enableHighAccuracy: true,
      timeout: 10000,
      maximumAge: 0,
    });
  } else {
    console.log("Geolocation is not supported by your browser");
  }
});

function successCallback(position) {
  const latitude = position.coords.latitude;
  const longitude = position.coords.longitude;

  // Update the map's center with user location
  new mapboxgl.Marker().setLngLat([longitude, latitude]).addTo(map);
  map.flyTo({
    center: [longitude, latitude],
    zoom: 12,
    speed: 1.5,
    essential: true,
  });

  convertCoordinate(longitude, latitude);
}

function errorCallback(error) {
  console.log(error);
}

function convertCoordinate(longitude, latitude) {
  const holder = document.querySelector("#search-input");
  var url = `https://api.mapbox.com/geocoding/v5/mapbox.places/${longitude},${latitude}.json?access_token=${mapboxgl.accessToken}`;
  console.log(longitude, latitude);
  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      // Extract the address from the response
      console.log(data);
      var address = data.features[0].place_name;
      console.log(address);
      holder.placeholder = address;
    })
    .catch((error) => console.error("Error:", error));
}
