import http from "@/http-common";

class dataService {
    getHello(): Promise<any> {
        return http.get("todos/1")
    }
}
export default new dataService();