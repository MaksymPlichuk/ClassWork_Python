// import {useEffect, useState} from "react";
// import axios from "axios";
// import type {IUserItem} from "../types/users/IUserItem.ts";
import {useGetUsersQuery} from "../services/usersApi.ts";
import {useEffect} from "react";
import {isTokenExpired} from "../utils/jwt.ts";

const HomePage = () => {
    // const [isError, setUsers] = useState<IUserItem[]>([]);
    // const [isLoading, setLoading] = useState(true);
    // const [isError, setError] = useState<string | null>(null);

    const {data: myUsers, isLoading, isError} = useGetUsersQuery();

    //Залежить від 2 параметри і відносно нього виконується даний хук
    // useEffect(() => {
    //     //console.log("HomePage UseEffect");
    //     axios.get<IUserItem[]>("http://127.0.0.1:4099/api/users")
    //         .then((resp)=>{
    //             const {data} = resp;
    //             // console.log("Result server", data);
    //             setUsers(data); //Зберігаю дані у State
    //         })
    //         .catch(error => {
    //             console.log("Problem request", error);
    //             setError("Не вдалося завантажити список користувачів");
    //         })
    //         .finally(() => {
    //             setLoading(false);
    //         });
    //},[]);
    // useEffect(() => {
    //     console.log("Home page loaded");
    //     const token = localStorage.getItem("accessToken");
    //     isTokenExpired(token)
    // }, [])

    return (
        <div className="min-h-screen bg-slate-50 dark:bg-slate-950 transition-colors duration-300">
            <div className="max-w-4xl mx-auto px-6 py-20 text-center">

                {/* Badge */}
                <span className="
                    inline-flex items-center gap-2 mb-6
                    px-3 py-1 rounded-full text-xs font-medium
                    bg-indigo-50 dark:bg-indigo-500/15
                    text-indigo-600 dark:text-indigo-400
                    border border-indigo-100 dark:border-indigo-500/20
                ">
                    <span className="w-1.5 h-1.5 rounded-full bg-indigo-500 animate-pulse" />
                    Ласкаво просимо
                </span>

                {/* Heading */}
                <h1 className="
                    text-5xl md:text-6xl font-bold tracking-tight
                    text-slate-900 dark:text-slate-50
                    mb-4
                ">
                    Наші{" "}
                    <span className="
                        bg-gradient-to-r from-indigo-500 to-violet-600
                        bg-clip-text text-transparent
                    ">
                        козаки
                    </span>{" "}
                    🐐
                </h1>

            </div>

            {/* Users table */}
            <div className="max-w-4xl mx-auto px-6 pb-20">
                <div className="
                    rounded-2xl overflow-hidden
                    border border-slate-200 dark:border-slate-800
                    bg-white dark:bg-slate-900
                    shadow-sm
                ">
                    {isLoading ? (
                        <div className="py-16 text-center text-slate-500 dark:text-slate-400">
                            Завантаження...
                        </div>
                    ) : isError ? (
                        <div className="py-16 text-center text-red-500 dark:text-red-400">
                            {isError}
                        </div>
                    ) : myUsers.length === 0 ? (
                        <div className="py-16 text-center text-slate-500 dark:text-slate-400">
                            Користувачів не знайдено
                        </div>
                    ) : (
                        <div className="overflow-x-auto">
                            <table className="w-full text-left text-sm">
                                <thead>
                                <tr className="
                                        bg-slate-50 dark:bg-slate-800/50
                                        border-b border-slate-200 dark:border-slate-800
                                    ">
                                    <th className="px-6 py-3 font-medium text-slate-500 dark:text-slate-400">Email</th>
                                    <th className="px-6 py-3 font-medium text-slate-500 dark:text-slate-400">Ім'я</th>
                                    <th className="px-6 py-3 font-medium text-slate-500 dark:text-slate-400">Прізвище</th>
                                    <th className="px-6 py-3 font-medium text-slate-500 dark:text-slate-400">Логін</th>
                                </tr>
                                </thead>
                                <tbody>
                                {myUsers.map((user) => (
                                    <tr
                                        key={user.id}
                                        className="
                                                border-b border-slate-100 dark:border-slate-800/60
                                                last:border-b-0
                                                hover:bg-slate-50 dark:hover:bg-slate-800/30
                                                transition-colors
                                            "
                                    >
                                        <td className="px-6 py-3 text-slate-900 dark:text-slate-100">{user.email}</td>
                                        <td className="px-6 py-3 text-slate-700 dark:text-slate-300">{user.first_name}</td>
                                        <td className="px-6 py-3 text-slate-700 dark:text-slate-300">{user.last_name}</td>
                                        <td className="px-6 py-3 text-slate-500 dark:text-slate-400">@{user.username}</td>
                                    </tr>
                                ))}
                                </tbody>
                            </table>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default HomePage;