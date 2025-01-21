document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById('clienteModal');
  
    modal.addEventListener('show.bs.modal', function (event) {
      const button = event.relatedTarget;
      const url = button.getAttribute('data-url');
  
      fetch(url)
        .then(response => response.text())
        .then(html => {
          document.getElementById('exibir-cliente').innerHTML = html;
        });
    });
  });


