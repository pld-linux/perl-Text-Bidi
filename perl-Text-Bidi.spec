#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Bidi
Summary:	Text::Bidi - Unicode bidi algorithm using libfribidi
Summary(pl.UTF-8):	Text::Bidi - algorytm Unicode bidi z użyciem libfribidi
Name:		perl-Text-Bidi
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	93e124628ff2983e32ac478f25f8d627
URL:		http://search.cpan.org/dist/Text-Bidi/
BuildRequires:	fribidi-devel >= 0.10.9
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Perl interface to the libfribidi library that implements the
Unicode bidi algorithm. The bidi algorithm is a specification for
displaying text that consists of both left-to-right and right-to-left
written languages.

%description -l pl.UTF-8
Ten moduł jest perlowym interfejsem do biblioteki libfribidi
implementującej algorytm Unicode bidi. Algorytm bidi jest specyfikacją
wyświetlania tekstu zawierającego tekst zarówno w językach pisanych od
lewej do prawej, jak i od prawej do lewej.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Text/Bidi.pm
%dir %{perl_vendorarch}/Text/Bidi
%{perl_vendorarch}/Text/Bidi/*.pm
%dir %{perl_vendorarch}/auto/Text/Bidi
%dir %{perl_vendorarch}/auto/Text/Bidi/private
%{perl_vendorarch}/auto/Text/Bidi/private/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Text/Bidi/private/*.so
%{_mandir}/man3/Text::Bidi.3pm*
%{_mandir}/man3/Text::Bidi::CapRTL.3pm*
