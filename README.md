# IO-Record-Form-API(English Version)
* Purpose：This API is designed to provide data to <a href="https://github.com/matthewcho1211/IO-Record-Form-Web" target="_blank">IO-Record-Form-Web</a>. The choice of front-end and back-end separation structure is because this project involves massive data processing. By doing so, we aim to simplify the code and loading on the website side.
* Feature：
  * This API handles all data <a href="https://github.com/matthewcho1211/IO-Record-Form-Web" target="_blank">IO-Record-Form-Web</a> requires.
  * Using RESTful API style design this API.
  * Deployed on the internet during development. Ensuring development and usage are not restricted by the local environment.
  * Implementing CI/CD processes, including automated testing, building, and deployment by GitHub Actions.
  * Using cache database store the data which frequently been used and calculated to reduce the loading on database.
* System Design：
    
  ![截圖 2024-01-02 下午2 55 00](https://github.com/musicboy0322/IO-Record-Form-Api/assets/75659334/6300cdc2-559b-4a16-a6b6-958149b305ec)

* Technique：
  * Programing Language：Python
  * Back-end Framework：Flask
  * Database：MySQL、Redis
  * CI/CD Tool：GitHub Actions
  * Deployment：Docker

# IO-Record-Form-API(中文版本)
* 目的：此 API 是用來提供資料給 <a href="https://github.com/matthewcho1211/IO-Record-Form-Web" target="_blank">IO-Record-Form-Web</a>。選擇此前後端分離架構，除了想練習此種形式以外，也因為此專案涉及到大量資料的處理。我們希望透過此方式減少網頁端那邊的處理以及並簡化其程式碼。
* 特色：
  * 此 API 處理所有 <a href="https://github.com/matthewcho1211/IO-Record-Form-Web" target="_blank">IO-Record-Form-Web</a> 需要的資料。
  * 採用 RESTful API 風格來設計此 API。
  * 專案進行時，此 API 有架設到網路上，讓開發和使用不受限於本地端。
  * 使用 GitHub Actions 來實現自動化 CI/CD 流程。
  * 使用快取資料庫儲存經常使用和計算的資料，以減少資料庫的負擔。
* 系統設計：

  ![截圖 2024-01-02 下午2 54 51](https://github.com/musicboy0322/IO-Record-Form-Api/assets/75659334/a24612c3-9306-4fc0-8c88-1901eaacdc83)

* 技術：
  * 編程語言：Python
  * 後端框架：Flask
  * 資料庫：MySQL、Redis
  * CI/CD 工具：GitHub Actions
  * 部署：Docker 
