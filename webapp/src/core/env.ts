export default class Env {
  public static get API_URL(): string {
    return process.env.VUE_APP_API_URL as string;
  }

  public static get WS_URL(): string {
    return process.env.VUE_APP_WS_URL as string;
  }
}
