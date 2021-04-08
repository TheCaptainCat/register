const fr = {
  app: {
    title: "Le Registre",
  },
  global: {
    cancel: "Annuler",
    save: "Sauvegarder",
  },
  components: {
    loader: {
      text: "Nous contactons le Registre",
      subtext: "Veuillez patienter",
    },
    dataTable: {
      pagination: "{start} à {end} sur {total}",
    },
    nav: {
      logout: "Déconnexion",
    },
  },
  views: {
    app: {
      error: {
        text: "Le Register est injoignable",
        subtext: "Contactez votre chef de chapitre",
      },
    },
    login: {
      header: "Bienvenue dans le Registre",
      subheader: "Communiquez vos identifiants",
      username: "Identifiant",
      password: "Mot de passe",
      btn: "Connexion",
    },
    home: {
      welcome: "Bienvenue dans le Registre du Conseil des Sorciers",
      private:
        "Le contenu de cette bibliothèque est strictement réservé aux sorcier assermentés",
      admin: {
        title: "Administration du Registre",
        manage_users: "Gérer les sorciers accrédités",
      },
      articles: {
        title: "Liste des articles",
        empty: "Aucun article n'existe dans ce langage",
        create: "Créer un article",
      },
      change_locale: "Changer de langue",
    },
    admin: {
      users: {
        title: "Gestion des sorciers accrédités",
        columns: {
          username: "Identifiant",
          email: "Adresse",
          roles: "Rôles",
        },
        add_role: "Ajouter",
        new_role: "Ajouter un rôle",
      },
    },
    article: {
      created: "créé par {name} le {date}",
      updated: "mis-à-jour par {name} le {date}",
      no_page: "Cet article n'existe pas dans cette langue",
      no_content: "Cet article est vide",
      not_found: "Cet article n'existe pas",
      edit: "Éditer",
      editor: "Section éditeur",
      translate: "Traduire cette page",
    },
    create_article: {
      title: "Création d'une nouvelle page",
      placeholder: "Nom de la page",
      btn: "Créer",
    },
  },
  api: {
    "user.login.wrong_credentials": "Informations incorrectes",
  },
};

export default fr;
