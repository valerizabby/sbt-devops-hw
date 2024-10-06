#!/bin/bash

timestamp=$(date +"%Y%m%d_%H%M%S")
log_file="monitor_${timestamp}.csv"

function start_monitoring {
    touch ${log_file}

    # запуск мониторинга
    (
        while true; do
            local current_date=$(date +"%Y-%m-%d")
            local disk_usage=$(df / | awk 'NR==2 {print $5}')
            local free_inodes=$(df -i / | awk 'NR==2 {print $4}')
            echo "$(date +"%Y-%m-%d %H:%M:%S"),${disk_usage},${free_inodes}" >> "${log_file}"

            # обновление лог-файла при переходе на новый день
            if [[ $(date +"%Y-%m-%d") != "$current_date" ]]; then
                timestamp=$(date +"%Y%m%d_%H%M%S")
                rm -f ${log_file}
                log_file="monitor_${timestamp}.csv"
                touch ${log_file}
            fi

            sleep 60 # интервал мониторинга в секундах
        done
    ) &
    echo $! > monitor.pid
    echo "Monitoring started with PID $!"
}

function stop_monitoring {
    if [[ -f monitor.pid ]]; then
        local pid=$(cat monitor.pid)
        if kill -0 $pid > /dev/null 2>&1; then
            kill $pid
            # зачищаем созданные файлы
            rm -f monitor.pid
            rm -f monitor_*
            echo "Monitoring stopped."
        else
            echo "No running process found."
        fi
    else
        echo "No PID file found. Monitoring may not be running."
    fi
}

function status_monitoring {
    if [[ -f monitor.pid ]]; then
        local pid=$(cat monitor.pid)
        if kill -0 $pid > /dev/null 2>&1; then
            echo "Monitoring is running with PID $pid."
        else
            echo "Monitoring is not running."
        fi
    else
        echo "Monitoring is not running."
    fi
}

case "$1" in
    START)
        start_monitoring
        ;;
    STOP)
        stop_monitoring
        ;;
    STATUS)
        status_monitoring
        ;;
    *)
        echo "Usage: $0 {START|STOP|STATUS}"
        ;;
esac