import { library } from "@fortawesome/fontawesome-svg-core";
import * as faIcons from "@fortawesome/free-solid-svg-icons";

const fontawesome = {
  install: (): void => {
    library.add(faIcons.faSpinner);
    library.add(faIcons.faExclamationCircle);
    library.add(faIcons.faSignInAlt);
  },
};

export default fontawesome;
