# Project_S2_Planning
Common repository for the ESAIP 2nd semester project

# Resources

- [tkcalendar](https://pypi.org/project/tkcalendar/)
- [python calendar module](https://docs.python.org/3/library/calendar.html)

# Git commands

## Commandes de base

- `git clone <repo_url_link>` : clone le repo depuis le cloud dans un dossier local
- `git fetch` : mettre à jour les références du cloud
- `git status` : comparer les changements entre le dossier local et le dernier commit
- `git pull` : mettre à jour le dossier local ("tirer" les changements du cloud)
- `git add <files_to_add>` : ajouter les changements pour un nouveau commit
- `git reset` : annuler `git add`
- `git commit -m "<commit_message>"` : faire un nouveau commit (une nouvelle photo)
- `git push` : mettre à jour le repo dans le cloud ("pousser" ses commits dans le cloud)

## Branches

- `git branch -a` : afficher toutes les branches (locales et distantes)
- `git branch <new_branch_name>` : créer une nouvelle branche en local
- `git switch <branch_name>` : changer de branche active
- `git push -u origin <new_branch>` : ajouter la branche sur le repo distant (avec tracking entre les branches locale et distante)
