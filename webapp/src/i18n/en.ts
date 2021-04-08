const en = {
  app: {
    title: "The Register",
  },
  global: {
    cancel: "Cancel",
    save: "Save",
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
      change_locale: "Change language",
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
    article: {
      created: "created by {name} on {date}",
      updated: "updated by {name} on {date}",
      no_page: "This article does not exist in this language",
      no_content: "This article is empty",
      not_found: "This article does not exist",
      edit: "Edit",
      editor: "Editor section",
      translate: "Translate this page",
    },
    create_article: {
      title: "Create a new page",
      placeholder: "Page's name",
      btn: "Create",
    },
  },
  api: {
    "user.login.wrong_credentials": "Wrong credentials",
  },
};

export default en;
