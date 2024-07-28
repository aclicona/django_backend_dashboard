const formatDate = (date) => {
    const date_ = new Date(date);
    let year = new Intl.DateTimeFormat("es", { year: "numeric" }).format(
        date_
    );
    let month = new Intl.DateTimeFormat("es", { month: "short" }).format(
        date_
    );
    let day = new Intl.DateTimeFormat("es", { day: "2-digit" }).format(date_);
    return `${day}/${month} ${year}`;
}
const shortDate = (date) => {
    const date_ = new Date(date);
    let month = new Intl.DateTimeFormat("es", { month: "short" }).format(
        date_
    );
    let day = new Intl.DateTimeFormat("es", { day: "2-digit" }).format(date_);
    return `${day}/${month}`;
}
const pluginformatDate = {
    install(app) {
        app.formatDate = formatDate
        app.config.globalProperties.$formatDate = formatDate

        app.shortDate = shortDate
        app.config.globalProperties.$shortDate = shortDate
    }
}

export { pluginformatDate }