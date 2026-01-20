import API from "@/config/apiClient";

export type User = {
  id: string;
  name: string;
  email: string;
  picture?: string;
};

export type SessionUser = {
  email?: string;
  name?: string;
  given_name?: string;
  family_name?: string;
  picture?: string;
  sub?: string;
};

export type Conversation = {
  _id: string;
  userId: string;
  title: string;
};

export type Message = {
  _id: string;
  userId: string;
  role: 'user' | 'assistant'
  content: string;
}

export type CreateUserPayload = Omit<User, "id">;
export type SendMessagePayload = Omit<Message, "_id">

export const getUser = (userId: string) =>
  API.get<User>("/user", { params: { user_id: userId } }).then(
    (res) => res.data
  );

export const createUser = (payload: CreateUserPayload) =>
  API.post<User>("/user", payload).then((res) => res.data);

export const getSessionUser = () =>
  API.get<SessionUser>("/auth/me").then((res) => res.data);

export const logout = () =>
  API.post("/auth/logout").then((res) => res.data)

export const getConversations = (userId: string) =>
  API.get<Conversation[]>("/conversation", {
    params: { user_id: userId },
  }).then((res) => res.data);

export const deleteConversations = (id: Conversation["_id"]) =>
  API.delete(`/conversation/${id}`);

export const sendMessage = (payload: SendMessagePayload) =>
  API.post<Message>("/message", payload).then((res) => res.data);

export const getMessages = (userId: string) =>
  API.get<Message[]>("/message", {
    params: { user_id: userId },
  }).then((res) => res.data);
