import {useGetUserQuery} from "../services/usersApi.ts";
import {useAppSelector} from "../store";

const ProfilePage = () => {

        //дістаємо user з RootState за цим хуком створеним у store/index.ts
    const user = useAppSelector(state => state.auth.user);
    const id = user?.id
    // не робить запит поки id ще немає
    const {data, isLoading, isError} = useGetUserQuery(id!, {skip: !id});

    return (
        <div className="max-w-4xl mx-auto px-6 pb-20">
            <div className="
                    rounded-2xl overflow-hidden
                    border border-slate-200 dark:border-slate-800
                    bg-white dark:bg-slate-900
                    shadow-sm
                ">
                {isLoading ? (
                    <div className="py-16 text-center text-slate-500 dark:text-slate-400">
                        Завантаженнуємо Дані Профілю...
                    </div>
                ) : isError ? (
                    <div className="py-16 text-center text-red-500 dark:text-red-400">
                        {isError}
                    </div>
                ) : data == null ? (
                    <div className="py-16 text-center text-slate-500 dark:text-slate-400">
                        Користувачів не знайдено
                    </div>
                ) : (
                    <div className="rounded overflow-hidden shadow-lg flex flex-row">
                                                                                                         {/*//костиль бо додається http*/}
                        <img className="w-full max-w-1/2 max-w-1/2" src={`http://127.0.0.1:4099/images/large/${data.image_large.split('/')[3]}`} alt="user image"/>
                        <div className="px-6 py-4">
                            <div className="font-bold text-xl mb-2">{data.username}</div>
                            <div className="font-bold text-sm mb-2">ID:{data.id}</div>
                            <p className="text-gray-700 text-xl"> {data.email} </p>
                            <p className="text-gray-700 text-base">{data.first_name} {data.last_name}</p>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
}
export default ProfilePage