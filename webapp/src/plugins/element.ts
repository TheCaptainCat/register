import { App } from "vue";
import ElementPlus from "element-plus";
import "../styles/element-variables.scss";

export default (app: App<Element>): void => {
  app.use(ElementPlus);
};
