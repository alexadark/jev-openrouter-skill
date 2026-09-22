# Grille de conseil OpenAI pour Jev

Version : 2026-09-22. Politique personnelle proposée à partir de la recherche de cette date, pas benchmark local validé ni classement universel. Périmètre : choix du modèle principal et de son effort pour une tâche code ou non-code. Cette grille ne remplace pas la politique d'exécution RIFF et n'autorise aucun routage automatique.

## Objectif prioritaire et axes séparés

Alexandra privilégie un résultat correct de bout en bout et le moins d'interventions humaines possible, particulièrement sur les exécutions longues. Le développement courant peut être peu complexe tout en exigeant une bonne continuité. Optimiser le coût total seulement après cette exigence de fiabilité, sans inventer un taux de réussite.

Distinguer dans le contexte envoyé à Jev :

- **Difficulté du raisonnement** : transformation connue, interactions à comprendre, ou diagnostic/planning ambigu.
- **Dépendance des étapes** : lot d'éléments indépendants et vérifiables, ou parcours où une erreur se propage aux étapes suivantes ; reprise après compaction possible.
- **Autonomie et détectabilité** : travail surveillé ou laissé sans intervention ; tests automatiques et parcours réels disponibles, ou défauts visibles seulement à la fin.
- **Coût d'une erreur tardive** : correction locale réversible, régression entre composants, incohérence de données ou reprise coûteuse.

La durée seule ne décide pas du modèle : 500 transformations indépendantes avec validation de schéma peuvent rester du travail Luna. Une fonctionnalité classique qui enchaîne données, interface, permissions et validation de parcours sans supervision peut justifier Astra même si aucun algorithme n'est difficile.

## Profils à transmettre dans `criteria`

Chaque ligne définit une option `choice`. Utiliser la colonne Profil comme clé et transmettre ensemble modèle, effort, usage et limites comme valeur. Ne pas envoyer uniquement le nom de l'option. Les clés sont des identifiants internes, pas des noms de modèles API.

| Profil | Modèle | Effort | Usage et limites |
| --- | --- | --- | --- |
| luna_low | gpt-5.6-luna | low | Traduction courte, titres, reformulation simple, classement, extraction exacte ou recherche ciblée d'un fichier connu. Faible ambiguïté et résultat facile à vérifier. Pas de choix architectural ni de décision sensible. |
| luna_medium | gpt-5.6-luna | medium | Inventaire délimité, extraction avec plusieurs contraintes, petit correctif à cause connue et test clair. Un long texte n'impose pas un grand modèle si le travail reste mécanique. |
| luna_high | gpt-5.6-luna | high | Implémentation bornée substantielle, contrats stabilisés, logique à plusieurs étapes et tests observables. Adapté à une unité vérifiable, pas choix par défaut pour porter seul une longue chaîne d'intégration sans supervision. Pas d'arbitrages produit, de permissions ou d'architecture encore ouverts. |
| luna_xhigh | gpt-5.6-luna | xhigh | Même périmètre borné, avec difficulté de raisonnement concrète non résolue à High ou explicitement démontrée. Exception, pas réglage par défaut pour extraction, inventaire ou tests. |
| sol_medium | gpt-5.6-sol | medium | Synthèse fidèle, préparation de réunion, rédaction soignée, recherche comparative cadrée ou développement courant. Premier candidat pour une exécution prolongée bien balisée avec contrats stables, étapes délimitées et validations automatiques solides. Préférer Astra Medium si les dépendances, la reprise de contexte ou les erreurs tardives rendent la supervision coûteuse. |
| sol_high | gpt-5.6-sol | high | Travail de niveau Sol avec contraintes imbriquées ou contradictions précises que Medium risque de mal résoudre. Pas une prime de fiabilité automatique pour toute tâche longue. Si le risque est surtout la dérive entre étapes ou la coordination transversale, considérer Astra Medium plutôt que monter l'effort par habitude. |
| astra_medium | gpt-6-astra | medium | Premier candidat pour une longue exécution autonome avec étapes interdépendantes, plusieurs outils/composants, reprises de contexte ou erreurs tardives coûteuses, même si le code est ordinaire. Aussi architecture, diagnostic ambigu, planning complexe, décision stratégique et acceptation visuelle exigeante. Peut être choisi directement ; ne pas imposer des échecs sur un petit modèle. Avantage attendu à tester sur le workflow réel, pas garantie d'absence d'erreurs. |
| astra_high | gpt-6-astra | high | Difficulté critique précisément identifiée, non résolue à Medium ou justifiant clairement une analyse plus profonde. Une seule passe bornée, puis retour à Medium après résolution. |
| astra_xhigh | gpt-6-astra | xhigh | Complexité exceptionnelle avec impasse documentée à High ou justification équivalente. Pas de choix automatique pour une grande phase, un long document ou une demande dite importante. |

Terra, GLM, DeepSeek, les autres modèles, Fast, Max et Ultra sont hors de cette grille initiale. C'est une restriction de périmètre, pas une affirmation d'infériorité. Si l'utilisateur demande explicitement une comparaison hors de cette liste, expliquer la limite et rechercher les éléments nécessaires avant de l'élargir ; ne pas substituer silencieusement un profil.

## Règles de décision à transmettre dans `state`

- Priorité : correction de bout en bout, puis interventions humaines évitables minimales, puis coût et durée totaux. Ne pas gagner quelques tokens si cela augmente plausiblement les régressions ou le besoin de supervision. Une approbation nécessaire ou un vrai blocage d'accès n'est pas une intervention évitable.
- Évaluer la nature du travail, l'ambiguïté, le nombre de systèmes liés, le coût d'une erreur, la possibilité de vérifier et les échecs déjà constatés. La longueur du prompt ou la taille d'un dépôt ne suffisent pas à classer la complexité.
- Distinguer transformation fidèle et synthèse interprétative : extraire des citations exactes peut relever de Luna ; relier des sources contradictoires ou construire un raisonnement relève plutôt de Sol ou Astra.
- Les outils, permissions et sources manquantes ne sont pas réparés par davantage de réflexion. Signaler ces limites au lieu de recommander automatiquement un modèle supérieur.
- Ne pas confondre budget de réflexion et endurance : High/XHigh n'est proposé que pour une difficulté de raisonnement identifiée. Pour une longue exécution, le maintien de l'état, la détection d'erreurs et les critères d'achèvement comptent aussi. Recommander les contrôles existants adaptés : étapes bornées, tests de parcours, checkpoint de décisions et blocages, reprise fondée sur les preuves. Ne pas installer un orchestrateur, multiplier les sous-agents ou ajouter des validations humaines pendant ce conseil.
- Pour une tâche simple, ne pas recommander Astra comme orchestrateur plus un worker : ce surcoût peut annuler l'économie. Le profil choisi est celui qui réalise la tâche, pas un plan de délégation.
- Un grand contexte peut coûter cher même avec peu de raisonnement. Réduire les lectures inutiles et distinguer entrée, cache et sortie. Ne pas confondre tarif API, crédits et quota de souscription Codex ; un changement de modèle peut aussi affecter le cache.
- Respecter le modèle explicitement imposé et les capacités actuellement connues du runtime. Si la disponibilité n'a pas été vérifiée, présenter le conseil comme conditionnel, pas comme une option déjà testée dans le sélecteur ou en sous-agent.
- Si plusieurs profils sont plausibles, préférer le moins coûteux seulement si la fiabilité attendue reste suffisante. Ne pas interpréter une probabilité de choix Jev comme un taux de réussite calibré. Signaler l'incertitude matérielle et l'hypothèse qui ferait changer le choix.

## Repères de validation

- Trois titres à partir d'un paragraphe fourni : candidat `luna_low` ; pas de recherche, pas de délégation.
- Transformer des données connues avec schéma explicite et tests : candidat `luna_medium` ou `luna_high` selon la logique.
- Synthétiser un transcript avec sélection et hiérarchisation des idées : candidat `sol_medium` ; ne pas déduire Astra de la seule longueur.
- Diagnostiquer une incohérence entre authentification, facturation et base de données, avec cause inconnue : candidat `astra_medium` ; pas de migration ou modification pendant le conseil.
- Développer plusieurs écrans CRUD avec contrats et tests stables, sans décisions ouvertes : candidat `sol_medium`, plutôt que Luna uniquement parce que chaque écran est simple.
- Livrer une fonctionnalité classique de bout en bout pendant une longue session sans supervision, entre données, permissions, UI et intégration, avec risques de régression tardive : candidat `astra_medium`, sans monter automatiquement à XHigh.

Ces repères évaluent la cohérence du conseil, pas une réponse obligatoire indépendamment des contraintes de la tâche.

## Sources et actualisation

Les capacités et niveaux sont à distinguer de la politique de choix ci-dessus. Sources consultées lors de la recherche du 22 septembre 2026 :

- [OpenAI, catalogue des modèles](https://developers.openai.com/api/docs/models) et [Luna](https://developers.openai.com/api/docs/models/gpt-5.6-luna) : identifiants et capacités. Le catalogue réel de l'application peut différer de l'API.
- [Artificial Analysis, efforts Luna](https://artificialanalysis.ai/models/releases/gpt-5-6-luna), [Sol](https://artificialanalysis.ai/models/releases/gpt-5-6-sol) et [Astra](https://artificialanalysis.ai/models/releases/gpt-6-astra) : compromis qualité/coût selon l'effort ; les valeurs dépendent du benchmark et de sa version.
- [Artificial Analysis, analyse Astra](https://artificialanalysis.ai/articles/benchmarking-gpt-6-astra) : gains agentiques, efficacité en tokens et limites selon le type de livrable.
- [Codex, tarification](https://learn.chatgpt.com/docs/pricing) : consommation dépendant du modèle, du contexte, des outils et du cache, pas seulement du nombre de messages.
- [METR, task-completion time horizons](https://metr.org/time-horizons/) : distingue fiabilité à 50 % et 80 %, et travail dépendant versus lots indépendants. L'horizon correspond au temps humain estimé, pas au nombre d'heures qu'un agent peut tourner. Cette page, mise à jour en mai 2026 lors de la consultation, ne départage pas directement Astra, Sol et Luna.
- [Anthropic, effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) : travail incrémental, état durable et tests pour limiter pertes de contexte et achèvement prématuré. Retour d'ingénierie sur Claude, pas preuve comparative sur les modèles OpenAI.

Les évaluations agentiques d'Artificial Analysis motivent l'essai d'Astra sur les chaînes longues, mais leurs résultats et efforts ne prouvent pas qu'Astra Medium bat Sol High dans RIFF. Pour valider ce choix, comparer sur les mêmes tâches et le même cadre : réussite complète, défauts/régressions détectés, interventions humaines évitables, temps humain de reprise et consommation totale. Distinguer les problèmes du modèle de ceux du contexte, des outils et des tests. Ne pas lancer ce benchmark ou changer RIFF pendant une simple consultation Jev.

Ne pas refaire une recherche complète à chaque conseil. Si la demande porte sur les performances actuelles, un nouveau modèle, ou si un profil devient indisponible, vérifier les sources concernées et signaler les limites de cette grille datée. Jev n'est pas chargé de rechercher ou d'inventer les benchmarks manquants.
