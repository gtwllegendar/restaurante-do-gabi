document.addEventListener('DOMContentLoaded', () => {
  const filters = document.querySelectorAll('.filter');
  const cards = document.querySelectorAll('.menu-item');
  filters.forEach((button) => {
    button.addEventListener('click', () => {
      const selected = button.dataset.filter;
      filters.forEach((item) => {
        const active = item === button;
        item.classList.toggle('active', active);
        item.setAttribute('aria-pressed', String(active));
      });
      cards.forEach((card) => {
        card.hidden = selected !== 'todos' && card.dataset.category !== selected;
      });
    });
  });

  const form = document.getElementById('contactForm');
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    document.getElementById('formFeedback').textContent =
      'Mensagem de demonstração preenchida. Configure um canal de atendimento para recebê-la.';
    form.reset();
  });

  document.getElementById('year').textContent = new Date().getFullYear();
});
