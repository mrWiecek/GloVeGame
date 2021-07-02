import http from "@/http-common";

class dataService {
    getAnalogies(word1: string, word2: string, word3: string): Promise<any> {
        return http.get("analogy/", { params: { word1: word1, word2: word2, word3:word3 } })
    }

    getClosestWords(word: string): Promise<any> {
        return http.get("closest/#{word}")
    }
}
export default new dataService();