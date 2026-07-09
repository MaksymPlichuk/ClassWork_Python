import {createSlice, type PayloadAction} from "@reduxjs/toolkit";
import type {AuthUser} from "../types/users/AuthUser.ts";
import {isTokenExpired} from "../utils/jwt.ts";
import type {RootState} from "../store";

//дані які повертає бек про User

interface AuthState {
    accessToken: string | null,
    refreshToken: string | null,
    user:  AuthUser | null,
}

function loadUserFormStorage(): AuthUser|null{
    const raw = localStorage.getItem("user");
    if (!raw) {return null}
    try {
        return JSON.parse(raw) as AuthUser;
    }catch {return null}
}

const initialState: AuthState = {
    accessToken: localStorage.getItem('accessToken'),
    refreshToken: localStorage.getItem('refreshToken'),
    user: loadUserFormStorage(),
}

const authSlice = createSlice({
    name: 'auth',
    initialState,
    // reducer: /* сама функція (state, action) => newState */,
    reducers: {
        setCredentials: (state, action: PayloadAction<{ access: string; refresh: string; user: AuthUser }>) => {
            const {access, refresh, user} = action.payload
            state.accessToken = access;
            state.refreshToken = refresh;
            state.user = user;

            localStorage.setItem('accessToken', access);
            localStorage.setItem('refreshToken', refresh);
            localStorage.setItem('user', JSON.stringify(user));
        },
        logout: (state) => {
            state.accessToken = null;
            state.refreshToken = null;
            state.user = null;

            localStorage.removeItem('accessToken');
            localStorage.removeItem('refreshToken');
            localStorage.removeItem('user');
        },
    }
})
export const {setCredentials, logout} = authSlice.actions;
export default authSlice.reducer; //authReducer  сама функція (state, action) => newState

//мій селектор який бере загальний стор (RootState) і закидує його у ф-цію, завдяки useSelector він при оновлені Store викликається
export const selectIsAuth = (state: RootState): boolean => {
    return !isTokenExpired(state.auth.accessToken);
}