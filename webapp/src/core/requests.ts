export interface FetchResponse<T> {
  code: number;
  data: T;
  messages: string[];
  status: string;
}

export type HttpMethod = "GET" | "POST" | "PUT" | "PATCH" | "DELETE";

export class FetchError<T> extends Error {
  public readonly request: FetchRequest<T>;
  public readonly code: number;
  public readonly errors: string[];

  constructor(request: FetchRequest<T>, code: number, errors: string[]) {
    super(
      `Fetch error ${code} ${request.method} ${request.domain}${request.path}`
    );
    this.request = request;
    this.code = code;
    this.errors = errors;
  }
}

export default class FetchRequest<T> {
  public readonly method: HttpMethod;
  public readonly domain: string;
  public readonly path: string;
  public readonly body?: T;

  public constructor(
    method: HttpMethod,
    domain: string,
    path: string,
    body?: T
  ) {
    this.method = method;
    this.domain = domain;
    this.path = path;
    this.body = body;
  }

  public async fetch<R>(): Promise<FetchResponse<R>> {
    let body: string | FormData | undefined;
    const headers = new Headers({
      Accept: "application/json",
    });
    if (this.body !== undefined) {
      if (this.body instanceof File) {
        body = new FormData();
        body.append("file", this.body);
      } else {
        body = JSON.stringify(this.body);
        headers.set("Content-Type", "application/json");
      }
    }
    const init: object = {
      body: body,
      credentials: "include",
      headers: headers,
      method: this.method,
      mode: "cors",
    };
    const fetchResponse = await fetch(
      new Request(this.domain + this.path, init),
      init
    );
    const response = (await fetchResponse.json()) as FetchResponse<R>;
    if (Math.floor(response.code / 100) !== 2)
      throw new FetchError<T>(this, response.code, response.messages);
    return response;
  }
}
