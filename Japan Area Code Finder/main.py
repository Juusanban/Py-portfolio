import csv
import re
from pathlib import Path

CSV_FILE = Path(__file__).with_name("city_codes.csv")


def load_records():
    records = []

    if not CSV_FILE.exists():
        save_records(records)
        return records

    with CSV_FILE.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            city = row.get("city", "").strip()
            area_code = row.get("area_code", "").strip()

            if city and area_code:
                records.append({
                    "city": city,
                    "area_code": area_code
                })

    return records


def save_records(records):
    with CSV_FILE.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["city", "area_code"])
        writer.writeheader()
        writer.writerows(records)


def is_valid_area_code(area_code):
    return re.fullmatch(r"0\d{1,4}", area_code) is not None


def show_all(records):
    if not records:
        print("\nデータがありません。")
        return

    print("\n登録されている市外局番")
    print("-" * 30)

    for index, record in enumerate(records, start=1):
        print(f"{index}. {record['city']}：{record['area_code']}")


def find_by_city(records):
    city = input("都市名を入力してください: ").strip()

    for record in records:
        if record["city"] == city:
            print(f"{city}の市外局番は{record['area_code']}です。")
            return

    print("該当する都市が見つかりません。")


def find_by_code(records):
    area_code = input("市外局番を入力してください: ").strip()

    matches = [
        record["city"]
        for record in records
        if record["area_code"] == area_code
    ]

    if matches:
        print(f"{area_code}の都市: {', '.join(matches)}")
    else:
        print("該当する市外局番が見つかりません。")


def add_record(records):
    city = input("追加する都市名を入力してください: ").strip()
    area_code = input("市外局番を入力してください: ").strip()

    if not city:
        print("都市名を入力してください。")
        return

    if not is_valid_area_code(area_code):
        print("市外局番は0から始まる2〜5桁の数字で入力してください。")
        return

    if any(record["city"] == city for record in records):
        print("その都市はすでに登録されています。")
        return

    records.append({
        "city": city,
        "area_code": area_code
    })
    save_records(records)
    print("データを追加しました。")


def update_record(records):
    city = input("変更する都市名を入力してください: ").strip()

    for record in records:
        if record["city"] == city:
            new_area_code = input(
                f"新しい市外局番を入力してください（現在: {record['area_code']}）: "
            ).strip()

            if not is_valid_area_code(new_area_code):
                print("市外局番は0から始まる2〜5桁の数字で入力してください。")
                return

            record["area_code"] = new_area_code
            save_records(records)
            print("データを変更しました。")
            return

    print("該当する都市が見つかりません。")


def delete_record(records):
    city = input("削除する都市名を入力してください: ").strip()

    for record in records:
        if record["city"] == city:
            records.remove(record)
            save_records(records)
            print("データを削除しました。")
            return

    print("該当する都市が見つかりません。")


def main():
    records = load_records()

    while True:
        print("\n=== 日本の市外局番検索 ===")
        print("1. 都市名から検索")
        print("2. 市外局番から検索")
        print("3. 一覧を表示")
        print("4. データを追加")
        print("5. データを変更")
        print("6. データを削除")
        print("0. 終了")

        choice = input("番号を選択してください: ").strip()

        if choice == "1":
            find_by_city(records)
        elif choice == "2":
            find_by_code(records)
        elif choice == "3":
            show_all(records)
        elif choice == "4":
            add_record(records)
        elif choice == "5":
            update_record(records)
        elif choice == "6":
            delete_record(records)
        elif choice == "0":
            print("プログラムを終了します。")
            break
        else:
            print("0〜6の番号を入力してください。")


if __name__ == "__main__":
    main()
