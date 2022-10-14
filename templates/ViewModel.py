def ViewModel(name):
    return f"""
import {{ observable }} from 'mobx';
import {{ Inject, Service }} from 'typedi';
import {{ ViewModel }} from '@itcs/react-mvvm';
import {{ {name.capitalize()}Service }} from '../../service/{name}/{name.capitalize()}Service';

@Service('{name}ViewModel')
export class {name.capitalize()}ViewModel extends ViewModel {{
    /** Глобальный объект App */
    app = (window.globalThis as any).App
    /** Признак прав пользователя **/
    @observable isAdmin: boolean = this.app.getMainView().getViewModel().get().isAdmin;

    /** Инициализация ViewModel */
    onInit() {{}}

    @Inject('{name}Service') {name}Service: {name.capitalize()}Service;
}}
"""