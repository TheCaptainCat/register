import { createApp } from "vue";
import App from "@/views/app/App.vue";
import "./registerServiceWorker";
import router from "./router";

import "@mdi/font/css/materialdesignicons.min.css";
import "./styles/styles.scss";

const app = createApp(App);
app.use(router);
app.mount("#app");
