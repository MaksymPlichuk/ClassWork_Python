import {fetchBaseQuery} from "@reduxjs/toolkit/query";
import type {RootState} from "../store"
import APP_ENV from "../env";

export const createBaseQuery = (endpoint: string) => {
    return fetchBaseQuery({
        baseUrl: `${APP_ENV.API_URL}/api/${endpoint}`,
        //додаємо хедери
        prepareHeaders: (headers, {getState}) => {
                        //RootState — тип-опис форми всього стору (глобальний state), автоматично виведений з конфігурації в configureStore
            //Виклик getState() повертає весь поточний Redux-стан
                                                                        // type RootState = {
                                                                        //     usersApi: {...},  // кеш RTK Query
                                                                        //     auth: {
                                                                        //         accessToken: string | null, --саме це і витягуємо
                                                                        //         refreshToken: string | null,
                                                                        //         user: AuthUser | null,
                                                                        //     }
                                                                        // }
            const token = (getState() as RootState).auth.accessToken;
            if (token) {
                headers.set('Authorization', `Bearer ${token}`);
            }
            return headers;
        },

    });
}