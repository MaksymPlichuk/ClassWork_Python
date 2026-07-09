import {createApi} from "@reduxjs/toolkit/query/react";
import {createBaseQuery} from "../utils/createBaseQuery.ts";
import type {IUserItem} from "../types/users/IUserItem.ts";
import type {IUserResponse} from "../types/users/IUserResponse.ts";
import type {IUserRegistration} from "../types/users/IUserRegistration.ts";
import type {IUserLogin} from "../types/users/IUserLogin.ts";
import {serialize} from "object-to-formdata";
import type {AuthUser} from "../types/users/AuthUser.ts";

export const usersApi = createApi({
    baseQuery: createBaseQuery('users'),
    tagTypes: ['users'],
    reducerPath: "usersApi",
    endpoints: (builder) => ({

        getUsers: builder.query<IUserItem[], void>({
            query: () => {
                return {
                    url: '/',
                    method: 'GET'
                }
            }
        }),                         //повертає           //приймає
        registerUser: builder.mutation<IUserResponse, IUserRegistration>({
            //віддає
            query: (userData) => {
                return {
                    //має бути такий шлях як у atbapi/users/views.py
                    url: '/register/',
                    method: 'POST',
                    body: userData
                }
            }
        }),
        loginUser: builder.mutation<IUserResponse, IUserLogin>({
            query: (userData) => {
                const formdata = serialize(userData)
                return {
                    url: '/login/',
                    method: 'POST',
                    body: formdata
                }
            }
        }),
        getUser: builder.query<AuthUser, string>({
            query: (id: string) => {
                return {
                    url: `/${id}/`,
                    method: 'GET',
                }
            }
        })
    })
});

export const {
    useGetUsersQuery,
    useRegisterUserMutation,
    useLoginUserMutation,
    useGetUserQuery,
} = usersApi;