document.addEventListener("DOMContentLoaded", function () {
  const selects = Array.from(document.querySelectorAll("select[id^='trait']"));
  selects.forEach(s => {
    s.addEventListener("change", () => {
      const values = selects.map(x => x.value).filter(Boolean);
      const unique = new Set(values);
      if (unique.size !== values.length) {
        alert("You have selected a duplicate trait. Please choose distinct traits.");
      }
    });
  });
});
