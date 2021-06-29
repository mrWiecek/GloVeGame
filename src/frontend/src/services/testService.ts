import http from "@/http-common";

class dataService {
    getHello(): Promise<any> {
        return http.get("/")
    }
}
export default new dataService();