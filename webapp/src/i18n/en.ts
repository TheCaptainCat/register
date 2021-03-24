const en = {
  app: {
    title: "The Register",
  },
  components: {
    loader: {
      text: "We are reaching the Register",
      subtext: "Please wait",
    },
    dataTable: {
      pagination: "{start} to {end} of {total}",
    },
    nav: {
      logout: "Logout",
    },
  },
  views: {
    app: {
      error: {
        text: "The Register is unreachable",
        subtext: "Please contact your head of chapter",
      },
    },
    login: {
      header: "Welcome to the Register",
      subheader: "Please provide your credentials",
      username: "Username",
      password: "Password",
      btn: "Log in",
    },
    home: {
      welcome: "Welcome to the Register of the Council of Sorcerers",
      private:
        "The content of this library is strictly reserved for sworn sorcerers",
      admin: {
        title: "Register administration",
        manage_users: "Manage accredited sorcerers",
      },
      articles: {
        title: "List of articles",
        empty: "No article found in this language",
        create: "Create an article",
      },
    },
    admin: {
      users: {
        title: "Manage authorized sorcerers",
        columns: {
          username: "Username",
          email: "Address",
          roles: "Roles",
        },
        add_role: "Add",
        new_role: "Add role",
      },
    },
  },
  api: {
    "user.login.wrong_credentials": "Wrong credentials",
  },
};

export default en;
