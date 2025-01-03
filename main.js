import { UILayout } from "./UIlayout.js"

// 本專案採用 python + psd_tools 實作
// Github => UI Layout Tool by William 77
// 設計師設計完 psd 文件後，透過本轉換工具生成的 ui-assets 素材，在網頁還原設計稿的位置與圖案
// 可減少 css 操作設定，設計師與程式設計師減少介面核對時間，雙方 win win

window.addEventListener('DOMContentLoaded', () => {
    UILayout.sort((a, b) => a.layerIndex - b.layerIndex).forEach(info => {
        const img = document.createElement('div')
        img.style.position = 'absolute'
        img.style.width = info.width + 'px'
        img.style.height = info.height + 'px'
        img.style.left = info.left + 'px'
        img.style.top = info.top + 'px'
        img.style.background = `url(${info.path})`
        document.body.append(img)
    })
})