import java.util.ArrayList;
import java.util.List;

public class LibraryManagementSystem {
    private List<Book> books;
    private List<Member> members;

    public LibraryManagementSystem() {
        this.books = new ArrayList<>();
        this.members = new ArrayList<>();
    }

    public void addBook(Book book) {
        books.add(book);
    }

    public void registerMember(Member member) {
        members.add(member);
    }

    public void borrowBook(String memberId, String bookId) throws Exception {
        Member member = findMemberById(memberId);
        Book book = findBookById(bookId);
        if (book.isAvailable()) {
            book.setAvailable(false);
            member.borrowBook(book);
        } else {
            throw new Exception("Book is not available");
        }
    }

    private Member findMemberById(String memberId) throws Exception {
        for (Member member : members) {
            if (member.getId().equals(memberId)) {
                return member;
            }
        }
        throw new Exception("Member not found");
    }

    private Book findBookById(String bookId) throws Exception {
        for (Book book : books) {
            if (book.getId().equals(bookId)) {
                return book;
            }
        }
        throw new Exception("Book not found");
    }
}

class Book {
    private String id;
    private String title;
    private boolean available;

    public Book(String id, String title) {
        this.id = id;
        this.title = title;
        this.available = true;
    }

    public String getId() {
        return id;
    }

    public boolean isAvailable() {
        return available;
    }

    public void setAvailable(boolean available) {
        this.available = available;
    }
}

class Member {
    private String id;
    private String name;
    private List<Book> borrowedBooks;

    public Member(String id, String name) {
        this.id = id;
        this.name = name;
        this.borrowedBooks = new ArrayList<>();
    }

    public String getId() {
        return id;
    }

    public void borrowBook(Book book) {
        borrowedBooks.add(book);
    }
}