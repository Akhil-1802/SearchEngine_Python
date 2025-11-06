console.log("Its working");

let searchbtn = document.querySelector(".search-btn");
let query;

searchbtn.addEventListener("click", async () => {
  query = document.querySelector(".search-input").value;
  query = query.trim().toLowerCase();
  await fetch(`http://127.0.0.1:8000/search/${query}`);

  window.location.href = `http://127.0.0.1:8000/search/${query}`;
});

document.querySelectorAll(".result-card").forEach((card) => {
  card.addEventListener("click", async () => {
    
    text = card.firstElementChild.textContent
    window.location.href = `http://127.0.0.1:8000/text/${text}/`;
    
  });
});
