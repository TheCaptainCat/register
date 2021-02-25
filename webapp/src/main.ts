import { createApp } from "vue";
import App from "@/views/app/App.vue";
import "./registerServiceWorker";
import router from "./router";
import { i18n, fontawesome } from "@/plugins";

import "./styles/styles.scss";

const app = createApp(App);
app.use(router);
app.use(i18n, { default: "en" });
app.use(fontawesome);
app.mount("#app");
