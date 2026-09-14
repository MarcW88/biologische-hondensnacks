const siteMenu=document.querySelector('[data-menu]');
const siteNav=document.querySelector('[data-nav]');

function closeSubmenus(except=null){
  document.querySelectorAll('.nav-item.expanded').forEach(item=>{
    if(item===except)return;
    item.classList.remove('expanded');
    item.querySelector('[data-submenu-toggle]')?.setAttribute('aria-expanded','false');
  });
}

document.querySelectorAll('[data-submenu-toggle]').forEach(button=>{
  button.addEventListener('click',()=>{
    const item=button.closest('.nav-item');
    const expanded=!item.classList.contains('expanded');
    closeSubmenus(item);
    item.classList.toggle('expanded',expanded);
    button.setAttribute('aria-expanded',String(expanded));
  });
});

document.addEventListener('keydown',event=>{
  if(event.key!=='Escape')return;
  siteNav?.classList.remove('open');
  siteMenu?.setAttribute('aria-expanded','false');
  closeSubmenus();
});
