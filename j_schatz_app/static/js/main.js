const contactNav = document.getElementById("contactNav");
const aboutNav = document.getElementsByClassName("homeIcons")[0];
const aboutMe = document.getElementsByClassName("p-text")[0];
const contactForm = document.getElementsByClassName("contact-form")[0];

console.log("works");

aboutNav.addEventListener("click", function() {
  console.log("works1");
  contactForm.style.display = "none";
  aboutMe.style.display = "block";
});

contactNav.addEventListener("click", function() {
  console.log("works1");
  aboutMe.style.display = "none";
  contactForm.style.display = "block";
});

//object with all elments of the page
//elmebtsbyclassname returns a node list so we need to grab inital index similar to array
const elements = {
  home: document.getElementsByClassName("home")[0],
  about: document.getElementsByClassName("p-text")[0],
  contact: document.getElementsByClassName("contact-form")[0],
  swift: document.getElementsByClassName("circle-1")[0],
  vueJS: document.getElementsByClassName("circle-2")[0],
  netlify: document.getElementsByClassName("circle-3")[0]
};

//navbar elements
const nav = {
  home: document.getElementById("homeNav"),
  about: document.getElementById("aboutNav"),
  contact: document.getElementById("contactNav")
};

//functions for showing and hiding elements
const showHome = homeElement => {
  homeElement.style.display = "flex";
  homeElement.style.justifyContent = "space-around";
  homeElement.style.alignItems = "center";
};
const show = element => {
  element.style.display = "block";
};

const hide = element => {
  element.style.display = "none";
};

//click event listeners for displaying page content

nav.home.addEventListener("click", function() {
  hide(elements.about);
  hide(elements.contact);
  showHome(elements.home);
});

nav.about.addEventListener("click", function() {
  console.log("This works");
  hide(elements.home);
  hide(elements.contact);
  show(elements.about);
});

nav.contact.addEventListener("click", function() {
  hide(elements.home);
  hide(elements.about);
  console.log("thissss works");
  show(elements.contact);
});

//Getting All Input Text Objects
const username = document.forms["contact"]["username"];
const email = document.forms["contact"]["email"];
const message = document.forms["contact"]["message"];

//Getting All Error Display Objects
const usernameError = document.getElementById("name_error");
const emailError = document.getElementById("email_error");
const messageError = document.getElementById("message_error");

window.onload = function() {
  elements.about.style.display = "none";
  elements.contact.style.display = "none";
};
//elements.home => parent element
//create element once item is clicked
const createdElement = document.createElement("a");
elements.swift.addEventListener("click", function() {
  //const node = document.createTextNode("works");
  const created = elements.home.appendChild(createdElement);
  console.log(created);
});

elements.vueJS.addEventListener("click", function() {
  console.log("works");
});

elements.netlify.addEventListener("click", function() {
  console.log("works");
});
