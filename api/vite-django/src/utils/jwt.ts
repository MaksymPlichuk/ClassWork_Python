import {jwtDecode} from "jwt-decode";

interface JwtPayload {
    exp: number;
}

export function isTokenExpired(token: string | null): boolean{
    if (!token) return true;
    try {
        const decoded = jwtDecode<JwtPayload>(token);
        console.log(decoded.exp*1000, Date.now());
        return decoded.exp * 1000 < Date.now();
    } catch {return true;}
}