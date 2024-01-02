# IO-Record-Form-API(English Version)
* Purpose：This API is to provide data to <a href="https://github.com/matthewcho1211/IO-Record-Form-Web" target="_blank">IO-Record-Form-Web</a>. The reason why using this method is because this project will have massive data processing. We want to use this way to reduce website side’s code and loading.
* Feature：
  * Using RESTful API style design the API.
  * The API have been set up on internet so that developing will not been limited by local side.
  * Using CI/CD automatically finish testing, structuring and deploying by GitHub Actions.
  * Using cache database store the data which frequently been used and calculated, so it can reduce database’s loading.
* System Design：
    
  ![截圖 2024-01-02 下午2 55 00](https://github.com/musicboy0322/IO-Record-Form-Api/assets/75659334/6300cdc2-559b-4a16-a6b6-958149b305ec)

* Technique：
  * Programing Language：Python
  * Framework：Flask
  * Database：MySQL、Redis
  * CI/CD Tool：GitHub Actions
  * Deployment：Docker

# IO-Record-Form-API(中文版本)
* 目的：此 API 是用來提供資料給 <a href="https://github.com/matthewcho1211/IO-Record-Form-Web" target="_blank">IO-Record-Form-Web</a>。使用此方法的原因除了想練習此種形式以外，也是因為此專案會有大量資料的處理，想透過此方式減少網頁端那邊的處理以及程式碼。
* 特色：
  * 使用 RESTful API 風格設計。
  * 有將此 API 架設到網路上，開發不受限於本地端。
  * 使用 CI/CD 來自動化完成一部分的軟體開發週期。
  * 將經常使用到且需要運算的資料用快取記憶體儲存，用已減緩資料庫的負載量。
* 系統設計：

  ![截圖 2024-01-02 下午2 54 51](https://github.com/musicboy0322/IO-Record-Form-Api/assets/75659334/a24612c3-9306-4fc0-8c88-1901eaacdc83)

* 技術：
  * 編程語言：Python
  * 框架：Flask
  * 資料庫：MySQL、Redis
  * CI/CD 工具：GitHub Actions
  * 部署：Docker 
