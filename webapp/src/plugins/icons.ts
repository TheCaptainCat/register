import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import * as faIcons from "@fortawesome/free-solid-svg-icons";

import { App } from "vue";

const fontawesome = {
  install: (app: App<Element>): void => {
    library.add(faIcons.faSpinner);
    library.add(faIcons.faExclamationCircle);
    library.add(faIcons.faSignInAlt);
    app.component("fa-icon", FontAwesomeIcon);
  },
};

export default fontawesome;
