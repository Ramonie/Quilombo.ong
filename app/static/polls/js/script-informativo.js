function alerte() {
  let checkbox = document.getElementById("termos_de_contrato");
  if (checkbox.checked) {
    alert("Você confirmou que está de acordo com os nossos termos de uso!");
  } else {
    alert("O cliente não marcou o checkbox");
  }
}
