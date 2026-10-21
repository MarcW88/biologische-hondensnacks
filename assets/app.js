const menu = document.querySelector('[data-menu]');
const nav = document.querySelector('[data-nav]');
menu?.addEventListener('click', () => {
  const open = nav.classList.toggle('open');
  menu.setAttribute('aria-expanded', String(open));
  menu.setAttribute('aria-label', open ? 'Menu sluiten' : 'Menu openen');
});

// Give every scrollable table a keyboard entry point and an accessible name.
document.querySelectorAll('.guide-table-wrap').forEach(wrapper => {
  wrapper.tabIndex = 0;
  wrapper.setAttribute('role', 'region');
  wrapper.setAttribute('aria-label', 'Tabel — horizontaal scrollbaar');
});

const steps = [...document.querySelectorAll('[data-step]')];
if (steps.length) {
  const answers = {};
  let step = 0;
  const questions = document.querySelector('[data-questions]');
  const result = document.querySelector('[data-result-wrap]');
  const dots = [...document.querySelectorAll('.progress i')];
  const status = document.createElement('p');
  status.className = 'finder-status';
  status.setAttribute('role', 'status');
  status.setAttribute('aria-live', 'polite');
  questions.before(status);

  const purpose = {
    Training: ['/soorten/trainingssnacks/', 'Trainingssnacks kiezen'],
    Beloning: ['/gidsen/hoeveel-snacks-mag-een-hond-per-dag/', 'Hoeveel snacks per dag?'],
    Kauwen: ['/gidsen/welke-kauwsnack-voor-mijn-hond/', 'Een kauwsnack kiezen'],
    Puppy: ['/levensfase/hondensnacks-puppy/', 'Snacks voor puppy’s kiezen']
  };
  const need = {
    'Gevoelige maag': ['/voor-gevoelige-honden/hondensnacks-gevoelige-maag/', 'Uitleg over een gevoelige maag'],
    Graanvrij: ['/voor-gevoelige-honden/graanvrije-hondensnacks/', 'Wat betekent graanvrij?'],
    'Mono-eiwit': ['/voor-gevoelige-honden/mono-eiwit-hondensnacks/', 'Uitleg over mono-eiwit']
  };
  const focusHeading = element => {
    const heading = element.querySelector('h3');
    heading.tabIndex = -1;
    heading.focus();
  };
  function show(focus = true) {
    steps.forEach((element, index) => { element.hidden = index !== step; });
    dots.forEach((dot, index) => {
      dot.classList.toggle('on', index <= step);
      dot.setAttribute('aria-hidden', 'true');
    });
    status.textContent = `Stap ${step + 1} van ${steps.length}`;
    if (focus) focusHeading(steps[step]);
  }
  function showResult() {
    questions.hidden = true;
    result.hidden = false;
    result.querySelector('h3').textContent = 'Lees verder bij je keuzes';
    document.querySelector('[data-result]').textContent =
      `Je keuzes: ${answers.doel}, ${answers.behoefte}, ${answers.eiwit}. ` +
      'Hieronder vind je uitleg bij dit profiel. Dit is geen selectie van geschikte producten of voedingsadvies.';
    const primary = purpose[answers.doel];
    const cta = result.querySelector('a.btn');
    cta.href = primary[0];
    cta.textContent = primary[1];
    result.querySelector('.finder-reading')?.remove();
    const list = document.createElement('ul');
    list.className = 'finder-reading';
    const links = [need[answers.behoefte], answers.eiwit === 'Kip'
      ? ['/eiwit/kip/', 'Lees het etiket van snacks met kip']
      : ['/gidsen/wat-is-mono-eiwit/', `Eiwitbronnen controleren: ${answers.eiwit}`]];
    for (const entry of links.filter(Boolean)) {
      const item = document.createElement('li');
      const link = document.createElement('a');
      [link.href, link.textContent] = entry;
      item.append(link);
      list.append(item);
    }
    cta.before(list);
    status.textContent = 'Je keuzehulpen zijn beschikbaar.';
    focusHeading(result);
  }
  document.querySelectorAll('[data-choice]').forEach(button => {
    button.setAttribute('aria-pressed', 'false');
    button.addEventListener('click', () => {
      answers[button.dataset.key] = button.dataset.choice;
      button.parentElement.querySelectorAll('[data-choice]').forEach(other => {
        other.classList.toggle('picked', other === button);
        other.setAttribute('aria-pressed', String(other === button));
      });
      if (step < steps.length - 1) {
        step += 1;
        show();
      } else showResult();
    });
  });
  document.querySelector('[data-reset]').addEventListener('click', () => {
    step = 0;
    Object.keys(answers).forEach(key => delete answers[key]);
    questions.hidden = false;
    result.hidden = true;
    document.querySelectorAll('[data-choice]').forEach(button => {
      button.classList.remove('picked');
      button.setAttribute('aria-pressed', 'false');
    });
    show();
  });
  show(false);
}
