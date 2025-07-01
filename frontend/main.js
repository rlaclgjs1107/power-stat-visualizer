fetch("http://localhost:5000/ping")
    .then(res => res.json())
    .then(data => {
        console.log("Flask says:", data.message);
        d3.select("body").append("p").text("Hello World!");
    });
