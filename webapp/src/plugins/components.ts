import { App } from "vue";
import Input from "@/components/Input.vue";
import Form from "@/components/Form.vue";
import Button from "@/components/Button.vue";
import Card from "@/components/Card.vue";

const registerComponents = {
  install: (app: App<Element>): void => {
    app.component("reg-input", Input);
    app.component("reg-form", Form);
    app.component("reg-btn", Button);
    app.component("reg-card", Card);
  },
};

export default registerComponents;
