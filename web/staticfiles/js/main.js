const copyButtonLabel = "Copy Code";

// use a class selector if available
let blocks = document.querySelectorAll("pre");

blocks.forEach((block) => {
  // only add button if browser supports Clipboard API
  if (navigator.clipboard) {
    let button = document.createElement("button");

    button.innerText = copyButtonLabel;
    block.appendChild(button);

    button.addEventListener("click", async () => {
      await copyCode(block);
    });
  }
});

async function copyCode(block, button) {
  let code = block.querySelector("code");
  let text = code.innerText;

  await navigator.clipboard.writeText(text);

  // visual feedback that task is completed
  button.innerText = "Code Copied";

  setTimeout(() => {
    button.innerText = copyButtonLabel;
  }, 700);
}


const hamburger = document.querySelector("#hamburger");
const menu = document.querySelector("#menu");
const hamElements = document.querySelectorAll("#ham-el");

hamburger.addEventListener('click', () => {
  menu.classList.toggle('hidden');
  
  hamElements.forEach(element => {
    element.classList.toggle('bg-white');
    element.classList.toggle('bg-black');
  });
});
