//Fazer a busca no images.google do que deseja
//abrir ferramentas do desenvolvedor e colar e executar o seguinte comando
//pode acontecer de ter que modificar o valor do querySelector se mudarem a estrutra da página
var urls = Array.from(document.querySelectorAll('.ivg-i h3:first-of-type a:first-of-type img:first-of-type')).filter(el=> !el['src'].toString().includes('data:image')).map(el=> el['src']);
window.open('data:text/csv;charset=utf-8,' + escape(urls.join('\n')));