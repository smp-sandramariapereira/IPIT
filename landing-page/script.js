const form = document.querySelector("#interest-form");
const status = document.querySelector("#form-status");

function setStatus(message, type = "") {
  status.textContent = message;
  status.className = `form-status field-full ${type}`.trim();
}

function clearInvalidState(field) {
  field.removeAttribute("aria-invalid");
}

function markInvalid(field) {
  field.setAttribute("aria-invalid", "true");
}

function validateForm() {
  const fields = [...form.querySelectorAll("input, select, textarea")];
  let firstInvalid = null;

  fields.forEach(clearInvalidState);

  for (const field of fields) {
    if (!field.checkValidity()) {
      markInvalid(field);
      firstInvalid ??= field;
    }
  }

  if (firstInvalid) {
    firstInvalid.focus();
    setStatus("Revise os campos obrigatórios antes de continuar.", "error");
    return false;
  }

  return true;
}

form.addEventListener("input", (event) => {
  if (event.target instanceof HTMLElement) {
    clearInvalidState(event.target);
  }
});

form.addEventListener("submit", (event) => {
  event.preventDefault();

  if (!validateForm()) {
    return;
  }

  const name = form.elements.nome.value.trim();
  form.reset();
  setStatus(
    `Interesse registrado apenas nesta demonstração, ${name}. Nenhum dado foi enviado ou armazenado.`,
    "success",
  );
});
