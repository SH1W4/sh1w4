# 📝 Como Gerenciar Seus Projetos no Perfil

Este perfil usa um **sistema modular** para facilitar a adição/remoção de projetos.

## 🚀 Adicionar Novo Projeto (30 segundos)

1. Abra `projects.json`
2. Adicione uma entrada na seção `"featured"` (projetos destacados) ou `"additional"` (biblioteca):

```json
{
  "name": "Nome do Projeto",
  "icon": "🚀",
  "type": "Categoria",
  "description": "Descrição concisa do que faz.",
  "url": "https://github.com/seu-usuario/repo",
  "status": "🟢 Active"
}
```

3. Rode o gerador:
```bash
python generate_readme.py
```

4. Commit e push:
```bash
git add .
git commit -m "feat: add new project to portfolio"
git push
```

## 🎨 Ícones Recomendados

- 🌐 Infraestrutura / Plataforma
- 📚 Documentação / Ferramenta
- 🛡️ Segurança / Legal
- ⚖️ IP / Patentes
- 🧠 AI / ML
- 🔬 Research / Deep Tech
- 🏗️ Arquitetura
- 🤖 Agentes / Automação

## 🏷️ Status Recomendados

- 🟢 **Active** - Em desenvolvimento ativo
- 🔵 **Stable** - Maduro e estável
- 🟣 **Evolving** - Design em evolução
- 🟡 **Alpha/Beta** - Experimental
- ⚪ **Archived** - Mantido mas não ativo

## 📦 Estrutura do Arquivo

- **featured**: Até 4-5 projetos (aparecem no perfil)
- **additional**: Projetos adicionais (backup, para referência)

## 🔄 Workflow Completo

1. Editar `projects.json`
2. Rodar `python generate_readme.py`
3. Verificar `README.md`
4. Commit e push

Simples assim! ✨
