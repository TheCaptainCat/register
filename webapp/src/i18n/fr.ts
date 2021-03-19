const fr = {
  app: {
    title: "Le Registre",
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
  },
  api: {
    "user.login.wrong_credentials": "Informations incorrectes",
  },
};

export default fr;
