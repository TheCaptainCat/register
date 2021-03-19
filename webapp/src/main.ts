import { createApp } from "vue";
import App from "@/App.vue";
import "./registerServiceWorker";
import router from "./router";
import element from "@/plugins/element";

import "@mdi/font/css/materialdesignicons.min.css";
import "./styles/styles.scss";

const app = createApp(App);
app.use(router);
app.use(element);
app.mount("#app");
