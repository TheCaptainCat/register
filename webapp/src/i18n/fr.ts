const fr = {
  app: {
    title: "Le Registre",
  },
  components: {
    loader: {
      text: "Nous contactons le Registre",
      subtext: "Veuillez patienter",
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
    },
  },
  api: {
    "user.login.wrong_credentials": "Informations incorrectes",
  },
};

export default fr;
